import * as React from 'react'

import { Header } from '@/components/global/header'
import { Hero } from '@/components/global/hero'
import { Footer } from '@/components/global/footer'

export default function RootPage() {
  return (
    <div>
      <Header />
      <main className="min-h-[80vh] pb-20 sm:pb-40">
        <Hero />
        <div className="container"></div>
      </main>
      <Footer />
    </div>
  )
}
