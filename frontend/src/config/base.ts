// src/config/configurations.ts
import { FieldConfig } from '@/types/base';
import { 
  FcDoughnutChart,
  FcBriefcase,
  FcWorkflow,
  FcSportsMode,
  FcTodoList,
  FcCollaboration,
  FcAreaChart,
  FcOrganization,
  FcSettings,
} from "react-icons/fc";

export const commonFields: Record<string, FieldConfig> = {
  created_at: {
    type: 'string',
    label: 'created_at',
    placeholder: 'Creation date',
    disabled: true,
    showInForm: false,
    showInTable: true,
  },
  updated_at: {
    type: 'string',
    label: 'updated_at',
    placeholder: 'Last update date',
    disabled: true,
    showInForm: false,
    showInTable: true,
  },
};

export const dashboardConfig = (t: (key: string) => string) => [
  {
  title: t('dashboard.metadata.title'),
  description: t('dashboardConfig.metadata.description'),
  },
]

export const siteConfig = (t: (key: string) => string) => [
  {
  title: t('site.metadata.title'),
  description: t('site.metadata.description'),
  },
]  

export const sideBarMenuItems = (t: (key: string) => string) => [
  {
    title: t('dashboard.sidebarMenu.dashboard'),
    href: "/main/dashboard",
    icon: FcDoughnutChart,
  },
  {
    title: t('dashboard.sidebarMenu.accounts'),
    href: "/main/accounts",
    icon: FcOrganization,
  },
  {
    title: t('dashboard.sidebarMenu.opportunities'),
    href: "/main/opportunities",
    icon: FcBriefcase,
  },
  {
    title: t('dashboard.sidebarMenu.projects'),
    href: "/main/projects",
    icon: FcWorkflow,
  },
  {
    title: t('dashboard.sidebarMenu.sprints'),
    href: "/main/sprints",
    icon: FcSportsMode,
  },
  {
    title: t('dashboard.sidebarMenu.tasks'),
    href: "/main/tasks",
    icon: FcTodoList,
  },
  {
    title: t('dashboard.sidebarMenu.daily_scrums'),
    href: "/main/dailyScrums",
    icon: FcCollaboration,
  },
  {
    title: t('dashboard.sidebarMenu.analytics'),
    href: "/main/analytics",
    icon: FcAreaChart,
  },
];

type BreadcrumbMapping = {
  [key: string]: string | ((param: string) => string);
};

export const breadcrumbMappings: BreadcrumbMapping = {
  '/accounts': 'accounts',
  '/accounts/[id]': (id: string) => `account ${id}`,
  '/accounts/register': 'registerAccount',
  '/daily_scrums': 'daily_scrums',
  '/daily_scrums/[id]': (id: string) => `dailyScrum ${id}`,
  '/daily_scrums/register': 'registerDailyScrum',
  '/opportunities': 'opportunities',
  '/opportunities/[id]': (id: string) => `opportunity ${id}`,
  '/opportunities/register': 'registerOpportunity',
  '/organizations': 'organizations',
  '/organizations/[id]': (id: string) => `organization ${id}`,
  '/organizations/register': 'registerOrganization',
  '/profile': 'profile',
  '/profile/[id]': (id: string) => `profile ${id}`,
  '/profile/register': 'registerProfile',
  '/projects': 'projects',
  '/projects/[id]': (id: string) => `project ${id}`,
  '/projects/register': 'registerProject',
  '/sprints': 'sprints',
  '/sprints/[id]': (id: string) => `sprint ${id}`,
  '/sprints/register': 'registerSprint',
  '/tasks': 'tasks',
  '/tasks/[id]': (id: string) => `task ${id}`,
  '/tasks/register': 'registerTask',
  '/site': 'site',
  '/site/page': 'sitePage',
  // Add other routes as needed
};

