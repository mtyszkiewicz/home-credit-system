<script lang="ts">
  import UserProfile from "../lib/UserProfile.svelte";
  import type { Activity } from "../types";
  import { page } from "$app/stores"
  const API_BASE = `http://${$page.url.hostname}:5055`;
  export let data;

  let activitiesDone: Activity[] = [];
  $: total = activitiesDone.reduce((acc, cur) => acc + cur.value, 0);
  $: score = data.user.score;

  async function handleClaimReward() {
    for (const activity of activitiesDone) {
      await fetch(
        `${API_BASE}/users/${data.user.id}/activity_records?activity_id=${activity.id}`,
        { method: "POST" }
      );
    }
    score += total;
    activitiesDone = [];
  }
</script>


<div
  class="p-6 mx-2 rounded-lg shadow-xl dark:bg-white/10 bg-white/30 ring-1 ring-gray-900/5 backdrop-blur-lg"
>
  <div class="flex place-content-around">
    <UserProfile username={data.user.name} image={data.user.image} {score} />
    {#if activitiesDone.length > 0}
      <button
        class="w-20 py-2 rounded-lg bg-opacity-25 ring-2 ring-blue-500 shadow-lg bg-blue-500 place-self-center"
        on:click={handleClaimReward}
      >
        Claim {total > 0 ? "+" : ""}{total}
      </button>
    {/if}
  </div>

  <div class="grid grid-cols-9 place-items-center mt-6 space-y-2">
    {#each data.activities as activity (activity.id)}
      <span class={`${activity.value > 0 ? 'text-green-500' : 'text-red-500'}`}>
        {activity.value > 0 ? '+' : ''}{activity.value}
      </span>
      <span class="text-xl">{activity.icon}</span>
      <span class="font-sm text-lg col-span-6 place-self-start">
        {activity.name}
      </span>
      <input
        type="checkbox"
        bind:group={activitiesDone}
        value={activity}
        class={`p-3.5 place-self-end accent-blue-500`}
      />
    {/each}
  </div>
</div>
