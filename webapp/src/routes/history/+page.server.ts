import type { ActivityRecordsHistory } from '../../types';

export async function load({ url }) {
  const API_BASE: string = `http://hcs-backend:5055`;
  const historyRes = await fetch(`${API_BASE}/activity_records`);
  const history: ActivityRecordsHistory[] = await historyRes.json();

  return {
    history: history
  }
}
