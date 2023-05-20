<script>
  import UserProfile from "../../lib/UserProfile.svelte";
  export let data;
</script>

{#each data.summary as summary}
  <div
    class="w-full max-w-xl p-6 mb-6 mx-auto rounded-lg shadow-xl dark:bg-white/10 bg-white/30 ring-1 ring-gray-900/5 backdrop-blur-lg"
  >
    <UserProfile
      username={summary.user.name}
      image={summary.user.image}
      score={summary.user.score}
    />
      {#each summary.activity_summary as activity (activity.id)}
        <div class="flex items-center py-3 justify-end">
          <div class="space-x-1">
            <span class="text-xl">{activity.icon}</span>
            <span class="font-sm">{activity.name}</span>
            <span class="font-sm">x{activity.count}</span>
            <span class="font-sm">Total: {activity.total_value}</span>
          </div>
        </div>
      {/each}
  </div>
{/each}
