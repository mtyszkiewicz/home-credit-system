<script lang="ts">
  import type { User } from "../types";
  export let user: User;
  export let score: number;
</script>

<div class="p-4 items-center">
  <div class="flex items-center space-x-4 place-content-start">
    <img
      src={user.image}
      alt={user.name}
      width={80}
      height={80}
      class="rounded-full ring-1 ring-gray-900/5 shadow-lg"
    />
    <div class="space-y-1">
      <p class="font-medium text-xl leading-none">{user.name}</p>
      <div class="font-light">
        <span>score:</span>
        <span>{score}</span>
      </div>
    </div>
  </div>
</div>
