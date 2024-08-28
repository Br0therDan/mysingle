import { redirect } from 'next/navigation';

export default function Home({ params: { locale },}: { params: { locale: string; };}) {
  return redirect('/site')
}
