// src/types/base.d.ts

import { z } from 'zod';
import { Tables } from './database.types';

// 필드 구성 타입 정의
export interface FieldConfig {
  type: string;
  label: string;
  placeholder?: string;
  options?: string[];
  disabled?: boolean | ((id?: string) => boolean);
  showInForm: boolean;
  showInTable: boolean;
  defaultValue?: any;
  linkTemplate?: string;
}

// 엔티티 구성 타입 정의
export interface BaseEntityConfig {
  fields: Record<string, FieldConfig>;  // 엔티티의 필드 구성 정의
  schema: z.ZodSchema;  // Zod 스키마를 사용하여 폼 데이터 검증
  identifierKey: keyof Tables['public']['Tables'];  // 고유 식별자 키
}

// entityConfigMap 타입 정의
export type EntityConfigMap = {
  accounts: BaseEntityConfig;
  dailyScrums: BaseEntityConfig;
  opportunities: BaseEntityConfig;
  organizations: BaseEntityConfig;
  profiles: BaseEntityConfig;
  projects: BaseEntityConfig;
  sprints: BaseEntityConfig;
  tasks: BaseEntityConfig;
};

// 각 엔티티별 기본 타입 정의
export type Account = Tables['public']['Tables']['accounts']['Row'];
export type DailyScrum = Tables['public']['Tables']['daily_scrums']['Row'];
export type Opportunity = Tables['public']['Tables']['opportunities']['Row'];
export type Organization = Tables['public']['Tables']['organizations']['Row'];
export type Profile = Tables['public']['Tables']['profiles']['Row'];
export type Project = Tables['public']['Tables']['projects']['Row'];
export type Sprint = Tables['public']['Tables']['sprints']['Row'];
export type Task = Tables['public']['Tables']['tasks']['Row'];
