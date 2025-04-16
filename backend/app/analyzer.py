from typing import Dict, Any
from .utils.html_parser import fetch_html, analyze_html
from .utils.header_analyzer import analyze_headers

def categorize_technologies(html_analysis: Dict[str, Any], header_analysis: Dict[str, Any]) -> Dict[str, Any]:
    tech_stack = {
        'frontend': {
            'framework': [],
            'libraries': [],
            'ui_frameworks': [],
            'features': []
        },
        'backend': {
            'framework': header_analysis.get('framework', ''),
            'server': header_analysis.get('server', ''),
            'language': ''
        },
        'infrastructure': {
            'cdn': header_analysis.get('cdn', ''),
            'caching': header_analysis.get('caching', {}),
            'security': header_analysis.get('security_headers', {})
        },
        'meta_info': {
            'description': '',
            'languages': [],
            'mobile_support': False,
            'seo_ready': False,
            'social_integration': []
        }
    }

    # フロントエンド分析
    frameworks = list(set(html_analysis.get('frameworks', [])))  # 重複を削除
    for framework in frameworks:
        if framework in ['React', 'Vue.js', 'Angular', 'Next.js', 'Nuxt.js']:
            tech_stack['frontend']['framework'].append(framework)

    # UIフレームワークとライブラリの分類
    for lib in html_analysis.get('libraries', []):
        if lib in ['Bootstrap', 'Tailwind CSS', 'Material-UI']:
            tech_stack['frontend']['ui_frameworks'].append(lib)
        else:
            tech_stack['frontend']['libraries'].append(lib)

    # 機能の分析
    tech_stack['frontend']['features'].extend(html_analysis.get('features', []))

    # バックエンド言語の推測
    if 'php' in header_analysis.get('x_powered_by', '').lower():
        tech_stack['backend']['language'] = 'PHP'
    elif 'python' in header_analysis.get('x_powered_by', '').lower():
        tech_stack['backend']['language'] = 'Python'
    elif 'node' in header_analysis.get('x_powered_by', '').lower() or 'Next.js' in frameworks:
        tech_stack['backend']['language'] = 'Node.js'

    # メタ情報の分析
    for meta in html_analysis.get('meta_tags', []):
        # 説明文
        if meta.get('name') == 'description':
            tech_stack['meta_info']['description'] = meta.get('content', '')
        
        # モバイル対応の検出
        if meta.get('name') == 'viewport':
            tech_stack['meta_info']['mobile_support'] = True

        # 言語の検出
        if meta.get('property') == 'og:locale':
            lang = meta.get('content', '').split('_')[0]
            tech_stack['meta_info']['languages'].append(lang)

    # SEO対策の検出
    if any(meta.get('name') in ['description', 'keywords'] for meta in html_analysis.get('meta_tags', [])):
        tech_stack['meta_info']['seo_ready'] = True

    # ソーシャル統合の検出
    if any(meta.get('property', '').startswith('og:') for meta in html_analysis.get('meta_tags', [])):
        tech_stack['meta_info']['social_integration'].append('Open Graph')
    if any(meta.get('name', '').startswith('twitter:') for meta in html_analysis.get('meta_tags', [])):
        tech_stack['meta_info']['social_integration'].append('Twitter Cards')

    return tech_stack

async def analyze_website(url: str) -> Dict[str, Any]:
    try:
        # HTMLの取得と分析
        html = await fetch_html(url)
        html_analysis = analyze_html(html)

        # ヘッダーの分析
        header_analysis = await analyze_headers(url)

        # 技術スタックの分類
        tech_stack = categorize_technologies(html_analysis, header_analysis)

        # 結果の統合
        result = {
            'url': url,
            'tech_stack': tech_stack,
            'security_score': len(header_analysis.get('security_headers', {})) * 20,  # 最大100点
            'mobile_friendly': tech_stack['meta_info']['mobile_support'],
            'seo_ready': tech_stack['meta_info']['seo_ready']
        }

        return result

    except Exception as e:
        return {
            'url': url,
            'error': str(e)
        } 