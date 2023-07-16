import { expect, test } from '@playwright/test';

test('404 page loads when page not found', async ({ page }) => {
  await page.goto('/bad');
  await expect(page).toHaveTitle(/404 Page not found/);
});

test('404 page has navbar', async ({ page }) => {
  await page.goto('/bad');
  await expect(page.locator('#navbar')).toBeVisible();
});
