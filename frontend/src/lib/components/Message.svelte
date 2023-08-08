<script lang="ts">
  export let messageId: string;
  export let message: string;
  export let showMessage = false;
  export let isError = false;
</script>

{#if showMessage}
  <div class="mt-2">
    {#if isError}
      <span id={messageId} class="text-error">{message}</span>
    {:else}
      <span id={messageId}>{message}</span>
    {/if}
  </div>
{/if}
