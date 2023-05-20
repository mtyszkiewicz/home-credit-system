<script>
  export let data;
</script>

<div class="place-content-start">
  {#each data.history as day}
    <p class="text-xl mt-4">{day.date}</p>
    <div class="divide-y divide-gray-900/5">
      {#each day.records as record (record.id)}
        <div class="flex items-center py-2 place-content-start pl-8">
          <div class="flex items-center space-x-4">
            <div class="space-x-1">
              <span class="text-sm text-gray-600">{record.time}</span>
              <span class="font-sm">{record.user.name}</span>
              <span class="font-sm">{record.activity.icon}</span>
              <span class="font-sm">{record.activity.name}</span>
            </div>
          </div>
        </div>
      {/each}
    </div>
  {/each}
</div>
