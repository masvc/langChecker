import aiohttp
from typing import Dict, Any

async def analyze_headers(url: str) -> Dict[str, Any]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            headers = response.headers
            server_info = {
                'server': headers.get('Server', ''),
                'x_powered_by': headers.get('X-Powered-By', ''),
                'content_type': headers.get('Content-Type', ''),
                'framework': '',
                'security_headers': {},
                'cdn': '',
                'caching': {}
            }

            # フレームワークの判定
            if 'X-Powered-By' in headers:
                powered_by = headers['X-Powered-By'].lower()
                if 'express' in powered_by:
                    server_info['framework'] = 'Express.js'
                elif 'php' in powered_by:
                    server_info['framework'] = 'PHP'
                elif 'python' in powered_by:
                    server_info['framework'] = 'Python'
                elif 'next.js' in powered_by:
                    server_info['framework'] = 'Next.js'
                elif 'nuxt' in powered_by:
                    server_info['framework'] = 'Nuxt.js'

            # セキュリティヘッダーの分析
            security_headers = [
                'X-Frame-Options',
                'X-Content-Type-Options',
                'X-XSS-Protection',
                'Content-Security-Policy',
                'Strict-Transport-Security',
                'Referrer-Policy'
            ]
            for header in security_headers:
                if header in headers:
                    server_info['security_headers'][header] = headers[header]

            # CDNの判定
            if 'Server' in headers:
                server = headers['Server'].lower()
                if 'cloudflare' in server:
                    server_info['cdn'] = 'Cloudflare'
                elif 'nginx' in server:
                    server_info['cdn'] = 'Nginx'
                elif 'apache' in server:
                    server_info['cdn'] = 'Apache'

            # キャッシュ設定の分析
            if 'Cache-Control' in headers:
                server_info['caching']['cache_control'] = headers['Cache-Control']
            if 'ETag' in headers:
                server_info['caching']['etag'] = headers['ETag']
            if 'Last-Modified' in headers:
                server_info['caching']['last_modified'] = headers['Last-Modified']

            return server_info 