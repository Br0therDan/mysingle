import { z } from 'zod';
import { BaseEntityConfig } from '@/types/base';
import { commonFields } from '@/config/base';

export const sprintsConfig: BaseEntityConfig = {
  identifierKey: 'sprint_id',
  fields: {
    sprint_name: {
      type: 'string',
      label: 'sprint_name',
      placeholder: 'Enter sprint name',
      disabled: (id?: string) => Boolean(id),
      showInForm: true,
      showInTable: true,
    },
    project_id: {
      type: 'string',
      label: 'project_id',
      placeholder: 'Select project',
      showInForm: true,
      showInTable: false,
    },
    goal: {
      type: 'string',
      label: 'goal',
      placeholder: 'Enter sprint goal',
      showInForm: true,
      showInTable: true,
    },
    start_date: {
      type: 'string',
      label: 'start_date',
      placeholder: 'Enter start date',
      showInForm: true,
      showInTable: true,
    },
    end_date: {
      type: 'string',
      label: 'end_date',
      placeholder: 'Enter end date',
      showInForm: true,
      showInTable: true,
    },
    status: {
      type: 'string',
      label: 'status',
      placeholder: 'Select status',
      options: ['Planned', 'In Progress', 'Completed'],
      showInForm: true,
      showInTable: true,
    },
    ...commonFields,
  },
  schema: z.object({
    sprint_name: z.string().nonempty("Sprint name is required"),
    project_id: z.string().nonempty("Project ID is required"),
    goal: z.string().optional(),
    start_date: z.string().nonempty("Start date is required"),
    end_date: z.string().nonempty("End date is required"),
    status: z.enum(['Planned', 'In Progress', 'Completed']),
    created_at: z.string().optional(),
    updated_at: z.string().optional(),
  }),
};
