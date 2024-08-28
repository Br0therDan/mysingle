'use client';

import TodayChart from "@/components/dashboard/chart/today";
import WeeklyChart from "@/components/dashboard/chart/weekly";

export default function DashboardPage() {
  return (
    <main className="grid flex-1 items-start gap-2 p-4 sm:px-6 sm:py-0 md:gap-4 lg:grid-cols-3 xl:grid-cols-3">
      <div className="grid auto-rows-max items-start gap-2 md:gap-4 lg:col-span-2">
        <h1 className="text-3xl pt-2 font-bold text-primary">Dashboard</h1>
        <p className="text-muted-foreground"> Welcome back</p>
        <div className="grid gap-4 sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-2 xl:grid-cols-4">
          <TodayChart />
          <WeeklyChart />
        </div>
      </div>
    </main>
  );
}
