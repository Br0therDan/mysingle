import { AlertCircle } from 'lucide-react'

import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'

export default function AlertDestructive(message: any) {
  return (
    <main className="flex items-center justify-center p-4 sm:px-6 sm:py-0 md:gap-8">
      <div className="flex h-screen w-full items-center justify-center">
        <Alert variant="destructive" className="max-w-96">
          <AlertCircle className="h-4 w-4" />
          <AlertTitle>Error</AlertTitle>
          <AlertDescription>{message.error}</AlertDescription>
        </Alert>
      </div>
    </main>
  )
}
