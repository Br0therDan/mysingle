"use client";
import Link from "next/link";
import { ChevronsLeft, ChevronsRight } from "lucide-react";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { sideBarMenuItems } from "@/config/base";
import { useSelector, useDispatch } from "react-redux";
import { FcSettings } from "react-icons/fc";
import { useTranslations } from "next-intl";
import { RootState } from "@/lib/redux/store";
import { collapseSidebar, expandSidebar } from "@/store/slices/sidebarSlice";

// 타입 선언
interface SideBarMenuItem {
  title: string;
  href: string;
  icon: React.ComponentType<any>;
}

export default function Sidebar() {
  const isExpanded = useSelector(
    (state: RootState) => state.sidebar.isExpanded
  );
  const dispatch = useDispatch();
  const t = useTranslations(); // i18n 훅 사용

  // `sideBarMenuItems` 함수 호출하여 배열 얻기
  const items = sideBarMenuItems(t);

  return (
    <>
      <aside
        className={`fixed inset-y-0 left-0 z-20 mt-14 hidden flex-col bg-slate-100 sm:flex ${
          isExpanded ? "w-64" : "w-16"
        } transition-all duration-300`}
      >
        {/* 네비게이션 메뉴 */}
        <nav className="flex flex-col gap-2 px-2 pt-5">
          <TooltipProvider>
            {items.map((item: SideBarMenuItem) => (
              <Tooltip key={item.title}>
                <TooltipTrigger asChild>
                  <Link
                    href={item.href}
                    className="flex h-9 text-sm text-black transition-colors hover:text-blue-600"
                  >
                    <div className="flex gap-3 pl-3">
                      <item.icon className="h-5 w-5" />
                      <span
                        className={`transition-opacity duration-300 ${
                          isExpanded ? "opacity-100" : "opacity-0"
                        }`}
                      >
                        {isExpanded && t(item.title)} {/* 다국어 지원 적용 */}
                      </span>
                    </div>
                  </Link>
                </TooltipTrigger>
                <TooltipContent
                  side="right"
                  className={`bg-black text-white ${
                    isExpanded ? "hidden" : ""
                  }`}
                >
                  {t(item.title)} {/* 다국어 지원 적용 */}
                </TooltipContent>
              </Tooltip>
            ))}
          </TooltipProvider>
        </nav>
        <nav className="mt-auto flex flex-col gap-2 px-2 pt-5">
          <TooltipProvider>
            <Tooltip>
              <TooltipTrigger asChild>
                <Link
                  href="#"
                  className="flex h-9 text-sm text-black transition-colors hover:text-blue-600"
                >
                  <div className="flex gap-3 pl-3">
                    <FcSettings className="h-5 w-5" />
                    <span
                      className={`w-auto transition-opacity duration-500 ${
                        isExpanded ? "opacity-100" : "opacity-0"
                      }`}
                    >
                      {isExpanded && t("dashboard.sidebarMenu.settings")}
                    </span>
                  </div>
                </Link>
              </TooltipTrigger>
              <TooltipContent
                side="right"
                className={`bg-black text-white ${isExpanded ? "hidden" : ""} `}
              >
                {t("DashboardConfig.SidebarMenu.settings")}{" "}
                {/* 다국어 지원 적용 */}
              </TooltipContent>
            </Tooltip>
          </TooltipProvider>
        </nav>

        {/* 사이드바 확장/축소 트리거 */}
        <nav
          className={`mt-0 flex gap-2 border-t p-5 ${
            isExpanded ? "justify-end" : "justify-center"
          }`}
        >
          {isExpanded ? (
            <ChevronsLeft
              className="h-5 w-5 cursor-pointer"
              onClick={() => dispatch(collapseSidebar())}
            />
          ) : (
            <div className="flex w-auto items-center justify-end gap-2">
              <ChevronsRight
                className="h-5 w-5 cursor-pointer"
                onClick={() => dispatch(expandSidebar())}
              />
            </div>
          )}
        </nav>
      </aside>
    </>
  );
}
