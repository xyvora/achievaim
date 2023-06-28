import { expect, test } from '@playwright/test';

test('page loads', async ({ page }) => {
  await page.goto('/create-goals');
  await expect(page.locator('#btnCreateGoal')).toBeVisible();
});
