// @/hooks/useProfile.ts

import useSWR from 'swr';
import axios from 'axios';

// fetcher 함수는 인자로 받은 키 배열에서 URL, 토큰, 이메일을 추출하여 요청을 수행합니다.
const fetcher = ([url, token, email]: [string, string, string]) => {
  return axios.get(url, {
    headers: {
      Authorization: `Bearer ${token}`,
      "X-User-Email": email,
    },
  }).then(res => res.data);
};

export const useProfile = () => {
  // /api/v1/token 및 /api/auth/me 엔드포인트에서 데이터를 각각 가져옵니다.
  const { data: tokenData, error: tokenError } = useSWR('/api/v1/token', (url) => fetch(url).then(res => res.json()));
  const { data: emailData, error: emailError } = useSWR('/api/auth/me', (url) => fetch(url).then(res => res.json()));

  // accessToken과 email을 추출합니다.
  const accessToken = tokenData?.accessToken;
  const email = emailData?.email;

  // profile 데이터 가져오기
  const { data: profile, error: profileError } = useSWR(
    // accessToken과 email이 모두 존재할 때만 fetcher를 호출합니다.
    () => (accessToken && email) ? [`${process.env.NEXT_PUBLIC_API_URL}/profiles/me`, accessToken, email] : null,
    fetcher
  );

  // 오류 처리 및 로딩 상태를 결합합니다.
  const loading = !profile && !profileError;
  const error = tokenError || emailError || profileError;

  return { profile, loading, error };
};



