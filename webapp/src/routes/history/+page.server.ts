import type { ActivityRecordsHistory } from '../../types';

export async function load({ url }) {
  const API_BASE: string = `http://${url.hostname}:5055`;
  const historyRes = await fetch(`${API_BASE}/activity_records`);
  const history: ActivityRecordsHistory[] = await historyRes.json();

  return {
    history: history
  }
}
