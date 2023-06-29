<div
  class="hero min-h-screen"
  style="background-image: url(/images/stock/photo-1507358522600-9f71e620c44e.jpg);"
>
  <div class="hero-overlay bg-opacity-60" />
  <div class="hero-content text-center text-neutral-content">
    <div class="max-w-md">
      <h1 class="mb-5 text-5xl font-bold">SMARTGoalAI</h1>
      <p class="mb-5">
        SMART Goal AI is a sophisticated tool leveraging artificial intelligence to assist users in
        formulating, tracking, and accomplishing their goals using the SMART (Specific, Measurable,
        Achievable, Relevant, Time-bound) methodology. It refines users' goals for clarity and
        realism and integrates features for tracking progress, including customizable reminders. The
        app promotes consistent habits by enabling users to schedule daily reminders, creating an
        effective and efficient platform for personal and professional growth.
      </p>
      <button class="btn btn-primary">More</button>
    </div>
  </div>
</div>
<div class="container mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl">
  <div class="mb-5">
    <label class="block text-gray-700 text-sm font-bold mb-2" for="goal"> Goal </label>
    <input
      class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
      id="goal"
      type="text"
      placeholder="Enter your goal"
    />
    <div class="mt-3">
      <button id="regenerate" class="btn btn-primary">Regenerate</button>
    </div>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Specific</h2>
          <p id="specific" class="text-gray-600" contenteditable="true">Information from API...</p>
        </figcaption>
      </figure>
    </div>
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Measurable</h2>
          <p id="measurable" class="text-gray-600" contenteditable="true">
            Information from API...
          </p>
        </figcaption>
      </figure>
    </div>
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Attainable</h2>
          <p id="attainable" class="text-gray-600" contenteditable="true">
            Information from API...
          </p>
        </figcaption>
      </figure>
    </div>
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Relevant</h2>
          <p id="relevant" class="text-gray-600" contenteditable="true">Information from API...</p>
        </figcaption>
      </figure>
    </div>
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Time-Bound</h2>
          <p id="time-bound" class="text-gray-600" contenteditable="true">
            Information from API...
          </p>
        </figcaption>
      </figure>
    </div>
  </div>
</div>

<div class="mt-4 flex flex-col items-center">
  <span class="text-gray-700 font-bold text-lg">Days of the week</span>
  <div class="mt-2 space-y-2 w-1/2">
    <div class="rounded shadow p-2">
      <label class="inline-flex items-center">
        <input
          type="checkbox"
          class="form-checkbox rounded text-indigo-600"
          name="days"
          value="Monday"
        />
        <span class="ml-2 text-gray-700 text-md">Monday</span>
      </label>
    </div>
    <div class="rounded shadow p-2">
      <label class="inline-flex items-center">
        <input
          type="checkbox"
          class="form-checkbox rounded text-indigo-600"
          name="days"
          value="Tuesday"
        />
        <span class="ml-2 text-gray-700 text-md">Tuesday</span>
      </label>
    </div>
    <div class="rounded shadow p-2">
      <label class="inline-flex items-center">
        <input
          type="checkbox"
          class="form-checkbox rounded text-indigo-600"
          name="days"
          value="Wednesday"
        />
        <span class="ml-2 text-gray-700 text-md">Wednesday</span>
      </label>
    </div>
    <div class="rounded shadow p-2">
      <label class="inline-flex items-center">
        <input
          type="checkbox"
          class="form-checkbox rounded text-indigo-600"
          name="days"
          value="Thursday"
        />
        <span class="ml-2 text-gray-700 text-md">Thursday</span>
      </label>
    </div>
    <div class="rounded shadow p-2">
      <label class="inline-flex items-center">
        <input
          type="checkbox"
          class="form-checkbox rounded text-indigo-600"
          name="days"
          value="Friday"
        />
        <span class="ml-2 text-gray-700 text-md">Friday</span>
      </label>
    </div>
    <div class="rounded shadow p-2">
      <label class="inline-flex items-center">
        <input
          type="checkbox"
          class="form-checkbox rounded text-indigo-600"
          name="days"
          value="Saturday"
        />
        <span class="ml-2 text-gray-700 text-md">Saturday</span>
      </label>
    </div>
    <div class="rounded shadow p-2">
      <label class="inline-flex items-center">
        <input
          type="checkbox"
          class="form-checkbox rounded text-indigo-600"
          name="days"
          value="Sunday"
        />
        <span class="ml-2 text-gray-700 text-md">Sunday</span>
      </label>
    </div>
  </div>
</div>

<div class="mt-4 flex flex-col items-center">
  <label class="block text-gray-700 text-lg font-bold mb-2" for="goal-time"> Time </label>
  <input
    class="shadow appearance-none border rounded w-1/2 py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
    id="goal-time"
    type="time"
  />
</div>
