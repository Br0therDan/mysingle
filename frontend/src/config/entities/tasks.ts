import { z } from 'zod';
import { BaseEntityConfig } from '@/types/base';
import { commonFields } from '@/config/base';

export const tasksConfig: BaseEntityConfig = {
  identifierKey: 'task_id',
  fields: {
    task_name: {
      type: 'string',
      label: 'task_name',
      placeholder: 'Enter task name',
      disabled: (id?: string) => Boolean(id),
      showInForm: true,
      showInTable: true,
    },
    assigned_to: {
      type: 'string',
      label: 'assigned_to',
      placeholder: 'Select assignee',
      showInForm: true,
      showInTable: true,
    },
    priority: {
      type: 'string',
      label: 'priority',
      placeholder: 'Select priority',
      options: ['Low', 'Medium', 'High'],
      showInForm: true,
      showInTable: true,
    },
    status: {
      type: 'string',
      label: 'status',
      placeholder: 'Select status',
      options: ['Not Started', 'In Progress', 'Completed'],
      showInForm: true,
      showInTable: true,
    },
    sprint_id: {
      type: 'string',
      label: 'sprint_id',
      placeholder: 'Select sprint',
      showInForm: true,
      showInTable: false,
    },
    description: {
      type: 'string',
      label: 'description',
      placeholder: 'Enter description',
      showInForm: true,
      showInTable: true,
    },
    ...commonFields,
  },
  schema: z.object({
    task_name: z.string().nonempty("Task name is required"),
    assigned_to: z.string().nonempty("Assignee is required"),
    priority: z.enum(['Low', 'Medium', 'High']),
    status: z.enum(['Not Started', 'In Progress', 'Completed']),
    sprint_id: z.string().nonempty("Sprint ID is required"),
    description: z.string().optional(),
    created_at: z.string().optional(),
    updated_at: z.string().optional(),
  }),
};
