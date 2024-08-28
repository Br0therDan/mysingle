'use client';
import DataTable from "@/components/dashboard/data-table";
import { columns, Org } from "./columns";
import { useEffect, useState } from 'react';
import axios from 'axios';
import LoadingPage from '@/components/global/loading-page';

export default function Page() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [scrumData, setScrumData] = useState<Org[]>([]);

  useEffect(() => {
    const fetchScrumData = async () => {
      setLoading(true);
      const url = `${process.env.NEXT_PUBLIC_BACKEND_API}/api/v1/orgs`;
      console.log("Fetching data from URL:", url); // URL 확인을 위한 로그 출력
      try {
        // 서버에서 액세스 토큰을 가져오는 API 호출
        const tokenResponse = await axios.get('/api/access-token');
        const accessToken = tokenResponse.data.accessToken;
        console.log("Access Token:", accessToken); // Access Token 확인을 위한 로그 출력

        // 액세스 토큰을 사용하여 데이터 가져오기
        const response = await axios.get(url, {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });
        console.log("API Response:", response.data); // API 응답 확인을 위한 로그 출력
        setScrumData(response.data);
      } catch (err) {
        console.error("Error fetching scrum data:", err); // 에러 로그 출력
        setError("Failed to fetch scrum data.");
      } finally {
        setLoading(false);
      }
    };

    fetchScrumData();
  }, []);

  if (loading) {
    return <LoadingPage />;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <main className="grid flex-1 items-start gap-4 p-4 sm:px-6 sm:py-0 md:gap-8">
      <h1 className="text-3xl font-bold text-primary">Daily Scrum</h1>
      <DataTable
        columns={columns}
        data={scrumData}
        title="Scrum Data"
        description="Scrum Data Overview"
      />
    </main>
  );
}
