import React, { useEffect, useState } from "react";
import { apiGet, apiPost } from "./api.js";

function money(n) {
  return `$${Number(n).toFixed(2)}`;
}

export default function App() {
  const [products, setProducts] = useState([]);
  const [health, setHealth] = useState("checking...");
  const [error, setError] = useState("");

  // Demo cart state (local-only, no API calls)
  const [cart, setCart] = useState({ items: [], subtotal: 0 });

  async function refresh() {
    setError("");
    try {
      const [h, p] = await Promise.all([
        apiGet("/health"),
        apiGet("/products"),
      ]);
      setHealth(h.status);
      setProducts(p);

      // Since /cart is removed from API, keep cart empty for now
      setCart({ items: [], subtotal: 0 });
    } catch (e) {
      setError(String(e.message || e));
    }
  }

  useEffect(() => {
    refresh();
  }, []);

  // Disable add-to-cart since API cart routes are removed
  async function add(productId) {
    setError("");
    try {
      const product = products.find((x) => x.id === productId);
      if (!product) return;

      // Local-only cart (demo)
      setCart((prev) => {
        const existing = prev.items.find((it) => it.product.id === productId);
        let nextItems;
        if (existing) {
          nextItems = prev.items.map((it) =>
            it.product.id === productId ? { ...it, quantity: it.quantity + 1 } : it
          );
        } else {
          nextItems = [
            ...prev.items,
            { id: `${productId}`, product, quantity: 1 },
          ];
        }

        const subtotal = nextItems.reduce(
          (sum, it) => sum + it.quantity * it.product.price,
          0
        );

        return { items: nextItems, subtotal: Number(subtotal.toFixed(2)) };
      });
    } catch (e) {
      setError(String(e.message || e));
    }
  }

  async function checkout() {
    setError("");
    try {
      const out = await apiPost("/checkout/create-session", {});
      alert(out.message);
    } catch (e) {
      setError(String(e.message || e));
    }
  }

  return (
    <div style={{ fontFamily: "system-ui, sans-serif", maxWidth: 960, margin: "0 auto", padding: 24 }}>
      <h1 style={{ marginBottom: 8 }}>E-Commerce (API-Driven) – UI</h1>
      <div style={{ opacity: 0.8, marginBottom: 16 }}>
        API health: <b>{health}</b>
      </div>

      {error && (
        <div style={{ padding: 12, background: "#ffe5e5", borderRadius: 10, marginBottom: 16 }}>
          <b>Error:</b> {error}
          <div style={{ marginTop: 8 }}>
            <button onClick={refresh}>Retry</button>
          </div>
        </div>
      )}

      <div style={{ display: "grid", gridTemplateColumns: "2fr 1fr", gap: 16, alignItems: "start" }}>
        <section style={{ padding: 16, border: "1px solid #eee", borderRadius: 16 }}>
          <h2>Products</h2>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(2, 1fr)", gap: 12 }}>
            {products.map((p) => (
              <div key={p.id} style={{ border: "1px solid #eee", borderRadius: 16, padding: 12 }}>
                <img src={p.image_url} alt={p.name} style={{ width: "100%", borderRadius: 12, marginBottom: 10 }} />
                <div style={{ fontWeight: 700 }}>{p.name}</div>
                <div style={{ opacity: 0.75, fontSize: 14, minHeight: 40 }}>{p.description}</div>
                <div style={{ marginTop: 8, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                  <div style={{ fontWeight: 700 }}>{money(p.price)}</div>
                  <button onClick={() => add(p.id)}>Add</button>
                </div>
              </div>
            ))}
          </div>
        </section>

        <aside style={{ padding: 16, border: "1px solid #eee", borderRadius: 16 }}>
          <h2>Cart (Local Demo)</h2>

          {cart.items.length === 0 ? (
            <div style={{ opacity: 0.75 }}>Your cart is empty.</div>
          ) : (
            <div style={{ display: "grid", gap: 10 }}>
              {cart.items.map((it) => (
                <div key={it.id} style={{ display: "flex", justifyContent: "space-between", gap: 12 }}>
                  <div>
                    <div style={{ fontWeight: 650 }}>{it.product.name}</div>
                    <div style={{ opacity: 0.75, fontSize: 14 }}>
                      {it.quantity} × {money(it.product.price)}
                    </div>
                  </div>
                  <div style={{ fontWeight: 700 }}>{money(it.quantity * it.product.price)}</div>
                </div>
              ))}
              <hr style={{ border: 0, borderTop: "1px solid #eee" }} />
              <div style={{ display: "flex", justifyContent: "space-between" }}>
                <div style={{ fontWeight: 700 }}>Subtotal</div>
                <div style={{ fontWeight: 900 }}>{money(cart.subtotal)}</div>
              </div>
              <button onClick={checkout}>Checkout</button>
              <div style={{ opacity: 0.6, fontSize: 12 }}>
                Checkout is demo-mode unless STRIPE_SECRET_KEY is set on the API.
              </div>
            </div>
          )}
        </aside>
      </div>

      <footer style={{ marginTop: 18, opacity: 0.7, fontSize: 13 }}>
        Tip: set <code>VITE_API_BASE_URL</code> in Render Static Site env vars.
      </footer>
    </div>
  );
}
