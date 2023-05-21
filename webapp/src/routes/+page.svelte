<script lang="ts">
  import UserProfile from "../lib/UserProfile.svelte";
  import Activity from "../lib/Activity.svelte";
  const API_BASE = "http://192.168.1.17:5055";
  export let data;

  $: score = data.user.score;

  /**
   * @param {bigint} activityId
   */
  async function publishNewActivityRecord(activityId: number) {
    await fetch(
      `${API_BASE}/users/${data.user.id}/activity_records?activity_id=${activityId}`,
      { method: "POST" }
    );
  }

  function handleActivityClick(event: CustomEvent) {
    const activityId = event.detail;
    publishNewActivityRecord(activityId);
    score += data.activities.find((a) => a.id === activityId)?.value ?? 0;
  }
</script>

<div
  class="w-full max-w-xl p-6 mx-2 rounded-lg shadow-xl dark:bg-white/10 bg-white/30 ring-1 ring-gray-900/5 backdrop-blur-lg"
>
  <UserProfile username={data.user.name} image={data.user.image} {score} />

  {#each data.activities as activity (activity.id)}
    <div class="flex items-center py-3 justify-end divide-y divide-gray-900/5">
      <Activity {activity} on:activityClick={handleActivityClick} />
    </div>
  {/each}
</div>
