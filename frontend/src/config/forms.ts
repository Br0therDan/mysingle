import * as z from "zod";

export const accountFormConfig = {
  schema: z.object({
    account_id: z.string(),
    account_name: z.string().min(1, "Account name is required"),
    account_type: z.string().min(1, "Account type is required"),
    owner: z.string().min(1, "Owner name is required"),
  }),
  fields: [
    {
      name: "account_name",
      label: "AccountForm.account_name",
      placeholder: "AccountForm.account_name",
      type: "text",
      disabled: true,
    },
    {
      name: "account_type",
      label: "AccountForm.account_type",
      placeholder: "AccountForm.account_type",
      type: "select",
      options: [
        { label: "Prospect", value: "Prospect" },
        { label: "Customer", value: "Customer" },
        { label: "Partner", value: "Partner" },
      ],
    },
    {
      name: "owner",
      label: "AccountForm.owner",
      placeholder: "AccountForm.owner",
      type: "text",
    },
  ],
};
