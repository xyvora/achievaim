<script lang="ts">
  import { themeChange } from 'theme-change';
  import { onMount } from 'svelte';
  onMount(() => {
    themeChange(false);
  });
</script>

<div class="m-5">
  🌞
  <div class="inline-block w-10">
    <span
      data-toggle-theme="light,dark"
      data-act-class="pl-4"
      class="border rounded-full border-primary flex items-center cursor-pointer w-10 transition-all duration-300 ease-in-out pl-0"
    >
      <span class="rounded-full w-3 h-3 m-1 bg-primary" />
    </span>
  </div>
  🌚
</div>
