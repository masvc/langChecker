from bs4 import BeautifulSoup
import aiohttp
from typing import List, Dict, Any
import re

async def fetch_html(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

def detect_framework_from_meta(meta_tags: List[Dict[str, str]]) -> List[str]:
    frameworks = []
    for meta in meta_tags:
        if meta.get('name') == 'generator':
            content = meta.get('content', '').lower()
            if 'wordpress' in content:
                frameworks.append('WordPress')
            elif 'drupal' in content:
                frameworks.append('Drupal')
        elif meta.get('name') == 'version' and 'ssr' in meta.get('content', '').lower():
            frameworks.append('Next.js')
    return frameworks

def detect_framework_from_script(script_tags: List[Dict[str, str]]) -> List[str]:
    frameworks = []
    for script in script_tags:
        src = script.get('src', '').lower()
        if 'react' in src:
            frameworks.append('React')
        elif 'vue' in src:
            frameworks.append('Vue.js')
        elif 'angular' in src:
            frameworks.append('Angular')
        elif 'next' in src:
            frameworks.append('Next.js')
        elif 'nuxt' in src:
            frameworks.append('Nuxt.js')
    return frameworks

def detect_libraries_from_script(script_tags: List[Dict[str, str]]) -> List[str]:
    libraries = []
    for script in script_tags:
        src = script.get('src', '').lower()
        if 'jquery' in src:
            libraries.append('jQuery')
        elif 'bootstrap' in src:
            libraries.append('Bootstrap')
        elif 'tailwind' in src:
            libraries.append('Tailwind CSS')
        elif 'material-ui' in src:
            libraries.append('Material-UI')
    return libraries

def detect_cms_from_html(html: str) -> List[str]:
    cms = []
    if 'wp-content' in html:
        cms.append('WordPress')
    if 'drupal' in html:
        cms.append('Drupal')
    if 'shopify' in html:
        cms.append('Shopify')
    return cms

def analyze_html(html: str) -> Dict[str, Any]:
    soup = BeautifulSoup(html, 'html.parser')
    technologies = {
        'frameworks': [],
        'libraries': [],
        'meta_tags': [],
        'server_info': [],
        'cms': [],
        'features': []
    }

    # metaタグの分析
    meta_tags = []
    for meta in soup.find_all('meta'):
        meta_data = {
            'name': meta.get('name', ''),
            'property': meta.get('property', ''),
            'content': meta.get('content', '')
        }
        meta_tags.append(meta_data)
        technologies['meta_tags'].append(meta_data)

    # scriptタグの分析
    script_tags = []
    for script in soup.find_all('script'):
        script_data = {
            'src': script.get('src', ''),
            'type': script.get('type', '')
        }
        script_tags.append(script_data)

    # linkタグの分析
    for link in soup.find_all('link'):
        href = link.get('href', '')
        if 'bootstrap' in href.lower():
            technologies['libraries'].append('Bootstrap')
        elif 'tailwind' in href.lower():
            technologies['libraries'].append('Tailwind CSS')
        elif 'material' in href.lower():
            technologies['libraries'].append('Material-UI')

    # フレームワークの検出
    technologies['frameworks'].extend(detect_framework_from_meta(meta_tags))
    technologies['frameworks'].extend(detect_framework_from_script(script_tags))

    # ライブラリの検出
    technologies['libraries'].extend(detect_libraries_from_script(script_tags))

    # CMSの検出
    technologies['cms'].extend(detect_cms_from_html(html))

    # 機能の検出
    if soup.find('form'):
        technologies['features'].append('Forms')
    if soup.find('input', {'type': 'search'}):
        technologies['features'].append('Search Functionality')
    if soup.find('a', {'href': re.compile(r'^https://twitter\.com')}):
        technologies['features'].append('Twitter Integration')
    if soup.find('a', {'href': re.compile(r'^https://facebook\.com')}):
        technologies['features'].append('Facebook Integration')

    return technologies 