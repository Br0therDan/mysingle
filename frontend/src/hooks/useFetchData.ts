import useSWR from "swr";
import axios from "axios";

const fetcher = async (url: string) => {
  const { accessToken } = await fetch("/api/v1/token").then((res) => res.json());
  const response = await axios.get(url, {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });
  if (!response.data) {
    throw new Error("Failed to fetch data");
  }
  return response.data;
};

export const useFetchData = <T>(url: string) => {
  const { data, error, isLoading } = useSWR<T>(url, fetcher);

  return {
    data: data || null,
    loading: isLoading,
    error: error ? error.message : null,
  };
};
