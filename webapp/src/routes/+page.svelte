<script>
  import UserProfile from "../lib/UserProfile.svelte";
  const API_BASE = "http://192.168.1.17:5055";
  export let data;

  $: score = data.user.score;

  /**
   * @param {bigint} activityId
   */
  async function logActivity(activityId) {
    await fetch(
      `${API_BASE}/users/${data.user.id}/activity_records?activity_id=${activityId}`,
      { method: "POST" }
    );
  }
</script>

<main
  class="relative flex flex-col items-center justify-center min-h-screen py-10"
>
  <div
    class="w-full max-w-xl p-12 mx-auto rounded-lg shadow-xl dark:bg-white/10 bg-white/30 ring-1 ring-gray-900/5 backdrop-blur-lg"
  >
    <UserProfile username={data.user.name} image={data.user.image} {score} />

    <div class="divide-y divide-gray-900/5">
      {#each data.activities as activity (activity.id)}
        <div class="flex items-center py-2 justify-end">
          <div class="flex items-center space-x-4">
            <div class="space-x-1">
              <span class="text-xl">{activity.icon}</span>
              <span class="font-sm leading-none">{activity.name}</span>
              <button
                class={`justify-self-end px-2 py-1 rounded shadow transition-colors duration-200 ${
                  activity.value > 0
                    ? "bg-green-500 text-white"
                    : "bg-red-500 text-white"
                }`}
                on:click={() => {
                  logActivity(activity.id);
                  score += activity.value;
                }}
              >
                {#if activity.value > 0}
                  +{activity.value}
                {:else}
                  {activity.value}
                {/if}
              </button>
            </div>
          </div>
        </div>
      {/each}
    </div>
  </div>
</main>

<style>
  .bg-green-500:hover {
    background-color: #047857; /* Adjust the shade as desired */
  }

  .bg-red-500:hover {
    background-color: #9f3a38; /* Adjust the shade as desired */
  }
</style>
