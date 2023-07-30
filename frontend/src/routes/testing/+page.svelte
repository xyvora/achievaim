<script lang="ts">
  import DaysOfWeekSelector from '$lib/components/DaysOfWeekSelector.svelte';
  import type { DaysOfWeek } from '$lib/generated';

  let daysOfWeek: DaysOfWeek = {
    monday: false,
    tuesday: false,
    wednesday: false,
    thursday: false,
    friday: false,
    saturday: false,
    sunday: false
  };

  let goalDate: string;
  let goalTime: string;
</script>

<div class="container pd-4 pb-4 rounded-xl shadow mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl z-10">
  <div class="card rounded-xl">
    <figure>
      <figcaption class="p-4 card-body">
        <div class="mb-5 primary">
          <label class="block text-xl font-bold mb-2" for="goal">Goal</label>
          <div
            class="shadow appearance-none rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
            id="goal"
          >
            Smart Goal
          </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          <!-- Specific card -->
          <div class="card">
            <figure>
              <figcaption class="p-4 card-body">
                <h2 class="card-title">Specific</h2>
                <div
                  id="specific"
                  class="shadow appearance-none rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                >
                  Specific Goal Information
                </div>
              </figcaption>
            </figure>
          </div>
          <!-- Measurable card -->
          <div class="card">
            <figure>
              <figcaption class="p-4 card-body">
                <h2 class="card-title">Measurable</h2>
                <div
                  id="measurable"
                  class="shadow appearance-none rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                >
                  Measurable Goal information
                </div>
              </figcaption>
            </figure>
          </div>
          <!-- Attainable card -->
          <div class="card">
            <figure>
              <figcaption class="p-4 card-body">
                <h2 class="card-title">Attainable</h2>
                <div
                  id="attainable"
                  class="shadow appearance-none rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                >
                  Attainable Goal information
                </div>
              </figcaption>
            </figure>
          </div>
          <!-- Relevant card -->
          <div class="card">
            <figure>
              <figcaption class="p-4 card-body">
                <h2 class="card-title">Relevant</h2>
                <div
                  id="relevant"
                  class="shadow appearance-none rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                >
                  Relevant Goal information
                </div>
              </figcaption>
            </figure>
          </div>
          <!-- Time-Bound card -->
          <div class="card">
            <figure>
              <figcaption class="p-4 card-body">
                <h2 class="card-title">Time-Bound</h2>
                <div
                  id="time-bound"
                  class="shadow appearance-none rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                >
                  Time-Bound Goal information
                </div>
              </figcaption>
            </figure>
          </div>
        </div>
      </figcaption>
    </figure>
    <figure class="flex flex-col md:flex-row">
      <div class="mt-4 p-4 flex flex-col items-center">
        <span class="block text-xl font-bold mb-2">Days Your SMART Goal Repeats:</span>
        <DaysOfWeekSelector {daysOfWeek} />
      </div>
      <div class="mt-4 p-4 flex flex-col items-center">
        <label class="block text-lg font-bold mb-2" for="goal-date">
          Date for Completing Your SMART Goal:
        </label>
        <input
          bind:value={goalDate}
          class="shadow appearance-none rounded-xl w-1/2 py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
          id="goal-date"
          type="date"
        />
        <label class="block text-lg font-bold mb-2 mt-4" for="goal-time">
          Time for Your SMART Goal Alert:
        </label>
        <input
          bind:value={goalTime}
          class="shadow appearance-none rounded-xl w-1/2 py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
          id="goal-time"
          type="time"
        />
      </div>
    </figure>
  </div>
</div>
<div class="flex">
  <div class="divider" />
</div>
