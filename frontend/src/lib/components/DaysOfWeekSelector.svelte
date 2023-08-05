<script lang="ts">
  import type { DaysOfWeek } from '$lib/generated';
  import { toTitleCase } from '$lib/utils';

  export let daysOfWeek: DaysOfWeek;
  export let readOnly = false;

  // Function to prevent changes to the checkbox state
  function handleCheckboxClick(event: Event) {
    event.preventDefault();
  }
</script>

<div class="grid sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-4 gap-5 mt-4">
  {#each Object.entries(daysOfWeek) as [day, value]}
    {#if day === 'monday' || day === 'tuesday' || day === 'wednesday' || day === 'thursday' || day === 'friday' || day === 'saturday' || day === 'sunday'}
      <div class="rounded-xl shadow p-2">
        <label class="inline-flex items-center">
          {#if !readOnly}
            <input
              type="checkbox"
              class={value ? 'toggle toggle-primary' : 'toggle toggle-info'}
              bind:checked={daysOfWeek[day]}
            />
          {:else}
            <input
              type="checkbox"
              class={value ? 'toggle toggle-primary' : 'toggle toggle-info'}
              checked={value}
              on:click={handleCheckboxClick}
            />
          {/if}
          <span class="ml-2 text-md">{toTitleCase(day)}</span>
        </label>
      </div>
    {/if}
  {/each}
</div>
