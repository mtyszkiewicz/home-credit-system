<script>
  const API_BASE = "http://192.168.1.17:5055";
  export let data;

  const username = data.userSummary.user.name;
  const image = data.userSummary.user.image;
  $: score = data.userSummary.user.total_score;

  function updateScore() {
    score += 1;
  }

  function refreshPage() {
    location.reload();
  }

  /**
   * @param {bigint} activityId
   */
  async function logActivity(activityId) {
    await fetch(
      `${API_BASE}/activities_log?user_id=${data?.user.id}&activity_id=${activityId}`,
      { method: "POST" }
    );
    location.reload();
  }
</script>

<main
  class="relative flex flex-col items-center justify-center min-h-screen py-10"
>
  {#if data?.user?.id}
    <div
      class="w-full max-w-xl p-12 mx-auto rounded-lg shadow-xl dark:bg-white/10 bg-white/30 ring-1 ring-gray-900/5 backdrop-blur-lg"
    >
    <div class="bg-red-500 p-6">
      <div class="flex items-center space-x-4">
        <img
          src={data?.user.image}
          alt={data?.user.name}
          width={64}
          height={64}
          class="rounded-full ring-1 ring-gray-900/5"
        />
        <div class="space-y-1">
          <p class="font-medium leading-none">{data?.user.name}</p>
          <p class="text-sm text-gray-500">Score: {score}</p>
        </div>
      </div>
    </div>

      <div class="divide-y divide-gray-900/5">
        {#each data?.activities as activity (activity.id)}
          <div class="flex items-center justify-between py-2">
            <div class="flex items-center space-x-4">
              <div class="space-x-1">
                <span class="font-sm leading-none">{activity.name}</span>
                <span class="text-xs text-gray-500">{activity.score}</span>
                <button
                  class="bg-gray-300 text-black px-2 py-1 rounded shadow hover:bg-gray-50 transition-colors duration-200"
                  on:click={() => logActivity(activity.id)}>Add</button
                >
              </div>
            </div>
          </div>
        {/each}
      </div>

      <!-- <div class="divide-y divide-gray-900/5">
        {#each data?.userSummary as summary (user.user_id)}
          <div class="flex items-center justify-between py-3">
            <div class="flex items-center space-x-4">
              <div class="space-x-1">
                <span class="font-medium leading-none">{user.user_name}</span>
                <span class="text-sm text-gray-500">{user.total_score}</span>
                <ul>
                  {#each user.activities as activity}
                    <li>{activity.activity_name} {activity.activity_count}</li>
                  {/each}
                </ul>
              </div>
            </div>
          </div>
        {/each}
      </div> -->
    </div>
  {:else}
    <h1 class="text-red-600 text-5xl font-bold text-center">
      UNKNOWN IDENTITY
    </h1>
  {/if}
</main>
