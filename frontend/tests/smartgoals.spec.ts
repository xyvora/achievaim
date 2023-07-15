import { expect, test } from '@playwright/test';

test('page loads', async ({ page }) => {
  await page.goto('/smartgoals');
  await expect(page.locator('#navbar')).toBeVisible();
});
