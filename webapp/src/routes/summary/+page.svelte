<script>
  import UserProfile from "../../lib/UserProfile.svelte";
  export let data;
</script>

{#each data.summary as summary}
  <div
    class="p-6 mb-6 mx-2 rounded-lg shadow-xl dark:bg-white/10 bg-white/30 ring-1 ring-gray-900/5 backdrop-blur-lg"
  >
    <div class="flex place-content-around">
      <UserProfile
        username={summary.user.name}
        image={summary.user.image}
        score={summary.user.score}
      />
    </div>
    <table class="w-full mt-3">
      <thead class="border-b-2 border-gray-300">
        <tr>
          <th class="text-left px-4 py-2">Activity</th>
          <th class="text-center px-4 py-2">Count</th>
          <th class="text-center px-4 py-2">Total Score</th>
        </tr>
      </thead>
      <tbody>
        {#each summary.activity_summary as activity (activity.id)}
          <tr class="border-b border-gray-200">
            <td class="flex items-center py-2 px-4">
              <span class="text-xl pr-1">{activity.icon}</span>
              <span class="ml-2">{activity.name}</span>
            </td>
            <td class="text-center py-2 px-4">{activity.count}</td>
            <td class="text-center py-2 px-4">{activity.total_value}</td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
{/each}
