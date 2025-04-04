<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>LICITA360 - Painel de Licitações</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet" />
  <style>
    body { font-family: 'Inter', sans-serif; background-color: #f5f7fa; margin: 0; padding: 0; }
    header { background-color: #1e40af; color: white; padding: 1rem; text-align: center; }
    .tabs { display: flex; gap: 1rem; margin: 1rem 2rem; }
    .tab-button { background-color: #e5e7eb; border: none; padding: 0.75rem 1.5rem; border-radius: 8px; cursor: pointer; }
    .tab-button.active { background-color: #2563eb; color: white; }
    main { padding: 0 2rem 2rem; }
    .search-bar { margin-bottom: 2rem; display: flex; gap: 1rem; }
    .search-bar input { flex: 1; padding: 0.75rem; border: 1px solid #ccc; border-radius: 8px; }
    .search-bar button { padding: 0.75rem 1.5rem; background-color: #2563eb; color: white; border: none; border-radius: 8px; cursor: pointer; }
    .results { background: white; border-radius: 12px; padding: 1.5rem; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); }
    .result-item { border-bottom: 1px solid #eee; padding: 1rem 0; }
    .result-item:last-child { border-bottom: none; }
    footer { text-align: center; padding: 1rem; font-size: 0.8rem; color: #666; }
    .tab-content { display: none; }
  </style>
</head>
<body>
  <header>
    <h1>LICITA360 - Painel de Licitações</h1>
  </header>

  <main>
    <div class="tabs">
      <button class="tab-button active" onclick="abrirAba(event, 'pncp')">🔍 PNCP</button>
      <button class="tab-button" onclick="abrirAba(event, 'comprasgov')">🏛 Compras.gov.br</button>
    </div>

    <div id="pncp" class="tab-content" style="display: block;">
      <div class="search-bar">
        <input type="text" id="searchInputPncp" placeholder="Buscar no PNCP..." />
        <button onclick="buscarPncp()">Buscar</button>
      </div>
      <section class="results" id="resultsPncp">
        <p>Digite um termo e clique em buscar para ver resultados do PNCP.</p>
      </section>
    </div>

    <div id="comprasgov" class="tab-content">
      <div class="search-bar">
        <input type="text" id="searchInputComprasgov" placeholder="Buscar no Compras.gov.br..." />
        <button onclick="buscarComprasGov()">Buscar</button>
      </div>
      <section class="results" id="resultsComprasgov">
        <p>Digite um termo e clique em buscar para ver resultados do Compras.gov.br.</p>
      </section>
    </div>
  </main>

  <footer>
    Desenvolvido por Benevaldo Craiba - LICITA360
  </footer>

  <script>
    function abrirAba(event, abaId) {
      document.querySelectorAll('.tab-content').forEach(aba => aba.style.display = 'none');
      document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));
      document.getElementById(abaId).style.display = 'block';
      event.target.classList.add('active');
    }

    async function buscarPncp() {
      const termo = document.getElementById("searchInputPncp").value;
      const results = document.getElementById("resultsPncp");
      results.innerHTML = "<p>Buscando no PNCP...</p>";

      try {
        const resposta = await fetch(`https://dados.gov.br/api/3/action/datastore_search?resource_id=8c10e5c3-d7e7-4c90-8d16-d46f62f5f2ee&q=${termo}`);
        if (!resposta.ok) throw new Error("Erro na API");

        const data = await resposta.json();
        const docs = data.result.records;

        if (!docs || docs.length === 0) {
          results.innerHTML = "<p>Nenhum resultado encontrado no PNCP.</p>";
          return;
        }

        results.innerHTML = "";
        docs.forEach(item => {
          const div = document.createElement("div");
          div.className = "result-item";
          div.innerHTML = `
            <strong>Objeto:</strong> ${item.objeto || "Não informado"}<br>
            <strong>Município:</strong> ${item.municipio || "Não informado"}<br>
            <strong>Data:</strong> ${item.data_abertura || "Não informado"}<br>
            <strong>Modalidade:</strong> ${item.modalidade || "Não informado"}<br>
            <strong>UF:</strong> ${item.uf || "Não informado"}
          `;
          results.appendChild(div);
        });
      } catch (error) {
        results.innerHTML = `<p>Erro ao buscar dados no PNCP: ${error.message}</p>`;
        console.error(error);
      }
    }
  </script>
</body>
</html>
