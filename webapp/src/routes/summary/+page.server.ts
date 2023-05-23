import type { UserActivitySummary } from "../../types";

const API_BASE: string = `http://${$page.url.hostname}:5055`;

export async function load() {
  const summaryRes = await fetch(`${API_BASE}/activity_summary`);
  const summary: UserActivitySummary[] = await summaryRes.json();

  return {
    summary: summary,
  };
}
