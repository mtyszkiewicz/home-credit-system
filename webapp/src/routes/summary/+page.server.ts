import { env } from "$env/dynamic/private";
import type { UserActivitySummary } from "../../types";

export async function load({ url }) {
  const summaryRes = await fetch(`${env.API_BASE_URL}/activity_summary`);
  const summary: UserActivitySummary[] = await summaryRes.json();

  return {
    summary: summary,
  };
}
