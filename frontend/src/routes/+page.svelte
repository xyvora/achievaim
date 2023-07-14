<script lang="ts">
  import { page } from '$app/stores';
</script>

<div class="hero min-h-screen bg-base-200 mb-10">
  <div class="flex flex-col lg:flex-row justify-around items-center lg:items-start hero-content">
    <div class="text-center lg:text-left lg:w-1/2">
      <h1 class="text-5xl font-bold">Smart Tracking Your Goals.</h1>
      <p class="py-6">
        SMART Goal AI is a sophisticated tool leveraging artificial intelligence to assist users in
        formulating, tracking, and accomplishing their goals using the SMART (Specific, Measurable,
        Achievable, Relevant, Time-bound) methodology. It refines users' goals for clarity and
        realism and integrates features for tracking progress, including customizable reminders. The
        app promotes consistent habits by enabling users to schedule daily reminders, creating an
        effective and efficient platform for personal and professional growth.
      </p>
    </div>
    <div class="card flex-shrink-0 w-full lg:w-1/3 max-w-sm shadow-2xl bg-base-100">
      <div class="card-body">
        <div class="form-control">
          <label class="label" for="email-input">
            <span class="label-text">Email</span>
          </label>
          <input type="text" placeholder="email" id="email-input" class="input input-bordered" />
        </div>

        <div class="form-control">
          <label class="label" for="password-input">
            <span class="label-text">Password</span>
          </label>
          <input
            type="password"
            placeholder="password"
            id="password-input"
            class="input input-bordered"
          />
          <a href={'#'} class="label-text-alt link link-hover mt-4 mb-4">Forgot password?</a>
          <a href="signup" class:active={$page.url.pathname === '/signup'}
          >Are your Goals Smart yet? Sign up here!</a
          >
        </div>
        <div class="form-control mt-6">
          <button class="btn btn-primary">Login</button>
        </div>
        <div class="form-control mt-6 text-center text-lg font-bold" />
      </div>
    </div>
  </div>
</div>
