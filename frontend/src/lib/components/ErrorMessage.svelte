<script lang="ts">
  export let errorMessageId: string;
  export let errorMessage: string;
  export let showError = false;
</script>

{#if showError}
  <div class="mt-2">
    <span id={errorMessageId} class="text-error">{errorMessage}</span>
  </div>
{/if}
