type StatusBadgeProps = {
  level: 'low' | 'medium' | 'high' | 'critical';
  text: string;
};

export const StatusBadge = ({ level, text }: StatusBadgeProps) => {
  return <span className={`badge ${level}`}>{text}</span>;
};
