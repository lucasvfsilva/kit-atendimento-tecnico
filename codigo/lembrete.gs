/**
 * Envia um e-mail com os clientes que precisam de contato hoje (ou atrasados).
 * Usa a aba "Clientes" da planilha. Configurar um acionador diário
 * em Acionadores > Baseado no tempo > Diário.
 */
function lembreteFollowUp() {
  const aba = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Clientes");
  const linhas = aba.getDataRange().getValues().slice(1); // pula o cabeçalho

  const hoje = new Date();
  hoje.setHours(0, 0, 0, 0);

  // Colunas: A=0 Empresa, B=1 Contato, C=2 Etapa, D=3 Próximo contato
  const pendentes = linhas
    .filter(l => l[0] && l[3] instanceof Date && l[3] <= hoje && !String(l[2]).startsWith("Fechado"))
    .map(l => `• ${l[0]}: falar com ${l[1]} (etapa: ${l[2] || "sem etapa"})`);

  if (pendentes.length === 0) return;

  MailApp.sendEmail(
    Session.getActiveUser().getEmail(),
    `Follow-ups de hoje: ${pendentes.length} cliente(s)`,
    pendentes.join("\n")
  );
}
