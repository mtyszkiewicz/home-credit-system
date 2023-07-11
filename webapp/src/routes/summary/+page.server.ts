import type { UserActivitySummary } from "../../types";

export async function load({ url }) {
  const API_BASE: string = `http://hcs-backend:5055`;
  const summaryRes = await fetch(`${API_BASE}/activity_summary`);
  const summary: UserActivitySummary[] = await summaryRes.json();

  return {
    summary: summary,
  };
}
