import { useState } from "react";

function Onboarding() {
  const [formData, setFormData] = useState({
    name: "",
    phone: "",
    city: "",
    platform: "",
    weeklyIncome: "",
    workingHours: ""
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
  e.preventDefault();

  const response = await fetch("http://127.0.0.1:8000/users/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      ...formData,
      weekly_income: Number(formData.weeklyIncome),
      working_hours: Number(formData.workingHours)
    })
  });

  const data = await response.json();
  console.log(data);
};

  return (
    <div style={{ maxWidth: "500px", margin: "auto" }}>
      <h2>Gig Worker Onboarding</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Full Name"
          value={formData.name}
          onChange={handleChange}
          required
        />

        <input
          type="text"
          name="phone"
          placeholder="Phone Number"
          value={formData.phone}
          onChange={handleChange}
          required
        />

        <input
          type="text"
          name="city"
          placeholder="City"
          value={formData.city}
          onChange={handleChange}
          required
        />

        <select
          name="platform"
          value={formData.platform}
          onChange={handleChange}
          required
        >
          <option value="">Select Platform</option>
          <option value="Swiggy">Swiggy</option>
          <option value="Zomato">Zomato</option>
          <option value="Amazon">Amazon</option>
          <option value="Zepto">Zepto</option>
        </select>

        <input
          type="number"
          name="weeklyIncome"
          placeholder="Average Weekly Income (₹)"
          value={formData.weeklyIncome}
          onChange={handleChange}
          required
        />

        <input
          type="number"
          name="workingHours"
          placeholder="Working Hours per Day"
          value={formData.workingHours}
          onChange={handleChange}
          required
        />

        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default Onboarding;