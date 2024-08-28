import * as React from 'react'
import { cn } from '@/lib/utils'

interface LogoProps extends React.ImgHTMLAttributes<HTMLImageElement> {}

const MyLogo = ({
  src = '/images/logo_sq_light.png', // 로고 이미지의 경로
  alt = 'MySigle', // 대체 텍스트
  width = '1024',
  height = '1024',
  className,
  ...props
}: LogoProps) => {
  return (
    <img
      src={src}
      alt={alt}
      width={width}
      height={height}
      className={cn('size-8 min-w-8', className)}
      {...props}
    />
  )
}

export { MyLogo, type LogoProps }
