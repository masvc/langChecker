document.addEventListener('DOMContentLoaded', () => {
    const urlInput = document.getElementById('urlInput');
    const analyzeButton = document.getElementById('analyzeButton');
    const loading = document.getElementById('loading');
    const error = document.getElementById('error');
    const results = document.getElementById('results');
    const resultsList = document.getElementById('resultsList');

    analyzeButton.addEventListener('click', async () => {
        const url = urlInput.value.trim();
        
        if (!url) {
            showError('URLを入力してください');
            return;
        }

        try {
            // 入力の検証
            new URL(url);
        } catch (e) {
            showError('有効なURLを入力してください');
            return;
        }

        // 分析開始
        showLoading();
        hideError();
        hideResults();

        try {
            const response = await fetch('http://localhost:8000/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url }),
            });

            if (!response.ok) {
                throw new Error('分析に失敗しました');
            }

            const data = await response.json();
            displayResults(data);
        } catch (err) {
            showError(err.message);
        } finally {
            hideLoading();
        }
    });

    function showLoading() {
        loading.classList.remove('hidden');
    }

    function hideLoading() {
        loading.classList.add('hidden');
    }

    function showError(message) {
        error.textContent = message;
        error.classList.remove('hidden');
    }

    function hideError() {
        error.classList.add('hidden');
    }

    function showResults() {
        results.classList.remove('hidden');
    }

    function hideResults() {
        results.classList.add('hidden');
    }

    function displayResults(data) {
        resultsList.innerHTML = '';
        
        if (data.error) {
            showError(data.error);
            return;
        }

        // フロントエンド技術
        const frontendTech = data.tech_stack.frontend;
        const frontendDetails = [
            frontendTech.framework.length ? `フレームワーク: ${frontendTech.framework.join(', ')}` : null,
            frontendTech.libraries.length ? `ライブラリ: ${frontendTech.libraries.join(', ')}` : null,
            frontendTech.ui_frameworks.length ? `UIフレームワーク: ${frontendTech.ui_frameworks.join(', ')}` : null,
            frontendTech.features.length ? `機能: ${frontendTech.features.join(', ')}` : null
        ].filter(Boolean).join('\n');
        
        if (frontendDetails) {
            addResultItem('フロントエンド技術', frontendDetails);
        }

        // バックエンド技術
        const backendTech = data.tech_stack.backend;
        const backendDetails = [
            backendTech.language ? `言語: ${backendTech.language}` : null,
            backendTech.framework ? `フレームワーク: ${backendTech.framework}` : null,
            backendTech.server ? `サーバー: ${backendTech.server}` : null
        ].filter(Boolean).join('\n');
        
        if (backendDetails) {
            addResultItem('バックエンド技術', backendDetails);
        }

        // インフラ情報
        const infraTech = data.tech_stack.infrastructure;
        const infraDetails = [
            infraTech.cdn ? `CDN: ${infraTech.cdn}` : null,
            Object.keys(infraTech.security).length ? `セキュリティヘッダー: ${Object.keys(infraTech.security).join(', ')}` : null
        ].filter(Boolean).join('\n');
        
        if (infraDetails) {
            addResultItem('インフラストラクチャ', infraDetails);
        }

        // メタ情報
        const metaInfo = data.tech_stack.meta_info;
        const metaDetails = [
            metaInfo.description ? `説明: ${metaInfo.description}` : null,
            metaInfo.languages.length ? `言語: ${metaInfo.languages.join(', ')}` : null,
            `モバイル対応: ${data.mobile_friendly ? 'あり' : 'なし'}`,
            `SEO対策: ${data.seo_ready ? 'あり' : 'なし'}`,
            metaInfo.social_integration.length ? `ソーシャル連携: ${metaInfo.social_integration.join(', ')}` : null
        ].filter(Boolean).join('\n');
        
        if (metaDetails) {
            addResultItem('メタ情報', metaDetails);
        }

        // セキュリティスコア
        addResultItem('セキュリティスコア', `${data.security_score}/100点`);

        showResults();
    }

    function addResultItem(title, content) {
        const item = document.createElement('div');
        item.className = 'result-item';
        
        const titleElement = document.createElement('h3');
        titleElement.textContent = title;
        
        const contentElement = document.createElement('pre');
        contentElement.textContent = content;
        
        item.appendChild(titleElement);
        item.appendChild(contentElement);
        resultsList.appendChild(item);
    }
}); 