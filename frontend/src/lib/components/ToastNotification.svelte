<script lang="ts">
  import { showToast, toastMessage } from '$lib/stores/stores';
</script>

{#if $showToast}
  <div class="toast" id="toast-message">
    <div class="alert alert-info">
      <span>{$toastMessage}</span>
    </div>
  </div>
{/if}
