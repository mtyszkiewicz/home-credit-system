<script>
  import { page } from "$app/stores";

  let who = $page.url.searchParams.get("who");
  const API_BASE = "http://192.168.1.17:5055"
  export let data;
  
  function refreshPage() {
		location.reload();
	};

  /**
   * @param {bigint} activityId
   */
  async function logActivity(activityId) {
    const res = await fetch(
      `${API_BASE}/activities_log?tenant_id=1&activity_id=${activityId}`,
      { method: "POST"}
    );
    const json = await res.json();
    location.reload();
  }
</script>

<main
  class="relative flex flex-col items-center justify-center min-h-screen py-10"
>
  {#if who}
    <div
      class="w-full max-w-xl p-12 mx-auto rounded-lg shadow-xl dark:bg-white/10 bg-white/30 ring-1 ring-gray-900/5 backdrop-blur-lg"
    >
      <div class="flex justify-between items-center">
        <p class="font-large">Aktywności</p>
        <button
          class="bg-gray-300 text-black px-2 py-1 rounded shadow hover:bg-gray-50 transition-colors duration-200"
          on:click={refreshPage}>Refresh Page</button
        >
      </div>

      <div class="divide-y divide-gray-900/5">
        {#each data?.activities as activity (activity.id)}
          <div class="flex items-center justify-between py-3">
            <div class="flex items-center space-x-4">
              <!-- <img
						src={user.image}
						alt={user.name}
						width={48}
						height={48}
						class="rounded-full ring-1 ring-gray-900/5"
					/> -->
              <div class="space-x-1">
                <span class="font-medium leading-none">{activity.name}</span>
                <span class="text-sm text-gray-500">{activity.score}</span>
                <button
                  class="bg-gray-300 text-black px-2 py-1 rounded shadow hover:bg-gray-50 transition-colors duration-200"
                  on:click={() => logActivity(activity.id)}>Add</button
                >
              </div>
            </div>
          </div>
        {/each}
      </div>
    </div>
  {:else}
    <h1 class="text-red-600 text-5xl font-bold text-center">
      UNKNOWN IDENTITY
    </h1>
  {/if}
</main>
