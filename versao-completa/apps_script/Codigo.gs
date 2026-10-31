/**
 * Recebe o diagnóstico enviado pelo diagnostico.py e adiciona uma linha
 * na aba "Inventário". Publicar em: Implantar > Nova implantação > App da Web.
 */
function doPost(e) {
  const d = JSON.parse(e.postData.contents);
  const aba = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Inventário");

  aba.appendRow([
    d.cliente,
    d.maquina,
    d.ram_total_gb,
    d.disco_livre_gb,
    d.nucleos_logicos,
    d.status,
    d.motivo,
    d.sistema,
    d.coletado_em,
  ]);

  return ContentService
    .createTextOutput(JSON.stringify({ ok: true }))
    .setMimeType(ContentService.MimeType.JSON);
}
