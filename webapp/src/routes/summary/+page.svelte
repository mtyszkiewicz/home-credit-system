<script>
  import UserProfile from "../../lib/UserProfile.svelte";
  export let data;
</script>

<div
  class="w-full max-w-xl p-6 mx-auto rounded-lg shadow-xl dark:bg-white/10 bg-white/30 ring-1 ring-gray-900/5 backdrop-blur-lg"
>
  <div class="divide-y divide-gray-900/5">
    {#each data.summary as summary}
      <UserProfile
        username={summary.user.name}
        image={summary.user.image}
        score={summary.user.score}
      />
      {#each summary.activity_summary as activity (activity.id)}
        <div class="flex items-center py-2 place-content-around">
          <div class="flex items-center space-x-4">
            <div class="space-x-1">
              <span class="text-xl">{activity.icon}</span>
              <span class="font-sm leading-none">{activity.name}</span>
              <span class="font-sm leading-none">x{activity.count}</span>
              <span class="font-sm leading-none"
                >Total: {activity.total_value}</span
              >
            </div>
          </div>
        </div>
      {/each}
    {/each}
  </div>
</div>
