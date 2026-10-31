/**
 * Envia um e-mail com os clientes que têm follow-up para hoje ou atrasado.
 * Configurar um acionador diário (Acionadores > Baseado no tempo > Diário).
 */
function lembreteFollowUp() {
  const aba = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Clientes");
  const linhas = aba.getDataRange().getValues().slice(1); // pula o cabeçalho

  const hoje = new Date();
  hoje.setHours(0, 0, 0, 0);

  // Colunas: A=0 Empresa, E=4 Etapa, G=6 Próximo contato, H=7 Próxima ação
  const pendentes = linhas
    .filter(l => l[0] && l[6] instanceof Date && l[6] <= hoje && !String(l[4]).includes("Fechado"))
    .map(l => `• ${l[0]} (${l[4]}): ${l[7] || "sem próxima ação definida"}`);

  if (pendentes.length === 0) return;

  MailApp.sendEmail(
    Session.getActiveUser().getEmail(),
    `Follow-ups de hoje: ${pendentes.length} cliente(s)`,
    pendentes.join("\n")
  );
}
