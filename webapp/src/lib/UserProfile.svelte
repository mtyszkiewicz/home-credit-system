<script>
  /** @type {string} */
  export let image;
  /** @type {string} */
  export let username;
  /** @type {number} */
  export let score;
</script>

<div class="p-4 items-center">
  <div class="flex items-center space-x-4 place-content-start">
    <img
      src={image}
      alt={username}
      width={80}
      height={80}
      class="rounded-full ring-1 ring-gray-900/5"
    />
    <div class="space-y-1">
      <p class="font-medium text-xl leading-none">{username}</p>
      <div class="font-light">
        <span>score:</span>
        <span>{score}</span>
      </div>
    </div>
  </div>
</div>
