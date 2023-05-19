<script>
  /** @type {string} */
  export let image;
  /** @type {string} */
  export let username;
  /** @type {number} */
  export let score;
</script>

<div class="bg-red-500 p-6">
  <div class="flex items-center space-x-4">
    <img
      src={image}
      alt={username}
      width={64}
      height={64}
      class="rounded-full ring-1 ring-gray-900/5"
    />
    <div class="space-y-1">
      <p class="font-medium leading-none">{username}</p>
      <p class="text-sm text-gray-500">Score: {score}</p>
    </div>
  </div>
</div>
