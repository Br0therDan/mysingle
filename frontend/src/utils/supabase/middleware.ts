import { createServerClient, type CookieOptions } from "@supabase/ssr";
import { type NextRequest, NextResponse } from "next/server";
import { createMiddlewareClient } from "@supabase/auth-helpers-nextjs";

export const createClient = (request: NextRequest) => {
  // Create an unmodified response
  let response = NextResponse.next({
    request: {
      headers: request.headers,
    },
  });

  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        get(name: string) {
          return request.cookies.get(name)?.value;
        },
        set(name: string, value: string, options: CookieOptions) {
          // If the cookie is updated, update the cookies for the request and response
          request.cookies.set({
            name,
            value,
            ...options,
          });
          response = NextResponse.next({
            request: {
              headers: request.headers,
            },
          });
          response.cookies.set({
            name,
            value,
            ...options,
          });
        },
        remove(name: string, options: CookieOptions) {
          // If the cookie is removed, update the cookies for the request and response
          request.cookies.set({
            name,
            value: "",
            ...options,
          });
          response = NextResponse.next({
            request: {
              headers: request.headers,
            },
          });
          response.cookies.set({
            name,
            value: "",
            ...options,
          });
        },
      },
    }
  );

  return { supabase, response };
};

export const updateSession = async (
  request: NextRequest,
  response: NextResponse
) => {
  try {
    // create a middleware to handle authentication
    const supabase = createMiddlewareClient({ req: request, res: response });
    const startTime = Date.now();
    // await supabase.auth.getUser();
    await supabase.auth.getSession();
    const endTime = Date.now();

    const duration = endTime - startTime;
    console.log('req', request.nextUrl.pathname)
    console.log(`미들웨어: 사용자 정보 확인 소요시간 지연：${duration} ms`);
    return response;
  } catch (e) {
    // If you are here, a Supabase client could not be created!
    // This is likely because you have not set up environment variables.
    // Check out http://localhost:3000 for Next Steps.
    return NextResponse.next({
      request: {
        headers: request.headers,
      },
    });
  }
};
