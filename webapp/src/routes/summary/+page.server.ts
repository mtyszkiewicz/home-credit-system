
const API_BASE: string = "http://192.168.1.17:5055";

export async function load() {
  const summary = fetch(`${API_BASE}/activity_summary`).then(res => res.json());

  return {
    summary: summary
  }
}